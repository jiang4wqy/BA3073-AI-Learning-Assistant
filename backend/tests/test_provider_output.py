from types import SimpleNamespace

import pytest

from backend.providers.base import TextGenerationRequest
from backend.providers.openai_compatible import OpenAICompatibleTextProvider


@pytest.mark.parametrize(
    ("base_url", "expected_body"),
    [
        ("https://api.deepseek.com/v1", {"thinking": {"type": "disabled"}}),
        ("https://dashscope.aliyuncs.com/compatible-mode/v1", None),
        ("https://api.deepseek.com.example.org/v1", None),
    ],
)
def test_artifact_generation_reserves_deepseek_budget_for_final_output(
    monkeypatch, base_url, expected_body
):
    def create(**kwargs):
        assert kwargs["extra_body"] == expected_body
        assert kwargs["max_tokens"] == 6000
        assert kwargs["messages"][1]["content"] == "Write a report."
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content="<html>Report</html>"))]
        )

    monkeypatch.setattr(
        "backend.providers.openai_compatible.resolve_api_key", lambda _: "test-api-key"
    )
    monkeypatch.setattr(
        "backend.providers.openai_compatible.OpenAI",
        lambda **_: SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create))),
    )
    result = OpenAICompatibleTextProvider().generate_text(
        TextGenerationRequest(
            profile={"base_url": base_url, "model": "example", "api_key_ref": "env:MODEL_API_KEY"},
            system_prompt="Return complete HTML.",
            user_prompt="Write a report.",
            max_output_tokens=6000,
            temperature=0.2,
        )
    )
    assert result == "<html>Report</html>"
