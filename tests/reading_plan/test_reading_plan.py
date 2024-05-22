from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest


def test_reading_plan_group_news(mock):
    reading_plan = ReadingPlanService()
    with pytest.raises(ValueError) as result:
        reading_plan.group_news_for_available_time(0)
    assert (
        str(result.value) == "Valor 'available_time' deve ser maior que zero"
    )

    mock.return_value = [
        {"title": "news1", "reading_time": 5},
        {"title": "news2", "reading_time": 10},
    ]

    expected = {
        "readable": [
            {
                "unfilled_time": 0,
                "chosen_news": [("news1", 5)],
            },
        ],
        "unreadable": [("news2", 10)],
    }
    assert reading_plan.group_news_for_available_time(5) == expected
