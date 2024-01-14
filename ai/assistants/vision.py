from typing import Optional

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

from ai.settings import ai_settings
from ai.storage import vision_assistant_storage


def get_vision_assistant(
    run_id: Optional[str] = None,
    user_id: Optional[str] = None,
    debug_mode: bool = False,
) -> Assistant:
    """Get a Vision Assistant"""

    return Assistant(
        name="vision_assistant",
        run_id=run_id,
        user_id=user_id,
        llm=OpenAIChat(
            model=ai_settings.gpt_4_vision,
            max_tokens=ai_settings.default_max_tokens,
            temperature=ai_settings.default_temperature,
        ),
        storage=vision_assistant_storage,
        monitoring=True,
        debug_mode=debug_mode,
        assistant_data={"assistant_type": "vision"},
    )
