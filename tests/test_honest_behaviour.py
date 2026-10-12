from elimu_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_an_unknown_exam_is_an_error_not_the_kcse_guide():
    r = _fn("exam_results_guide")("SAT")
    assert "error" in r and "kcse" in r["valid_exams"] and "full_name" not in r


def test_known_exams_still_work_in_any_case():
    assert "full_name" in _fn("exam_results_guide")("KCPE") and "full_name" in _fn("exam_results_guide")("kcse")
