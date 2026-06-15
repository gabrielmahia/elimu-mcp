"""ElimuMCP — Kenya Education System Navigation (5 tools). All data DEMO."""
from __future__ import annotations
from typing import Optional
from fastmcp import FastMCP

mcp = FastMCP(name="elimu-mcp", instructions="Kenya education system navigation. DEMO data only.")

@mcp.tool(name="school_finder", description="Find schools in a Kenya county by level. DEMO.")
def school_finder(county: str, level: Optional[str] = "secondary", school_type: Optional[str] = None) -> dict:
    levels = {"primary": "Standard 1-8, KCPE at end", "secondary": "Form 1-4, KCSE at end",
              "tvet": "6 months–3 years, NQF Level 2-5", "university": "3-4 year degree programs"}
    sample = [{"name": f"{county} High School", "level": level, "type": "public", "county": county, "board": "TSC/MOE"},
              {"name": f"St. Mary's {county}", "level": level, "type": "private", "county": county, "board": "Private"},
              {"name": f"{county} Girls School", "level": level, "type": "public", "county": county, "board": "TSC/MOE"}]
    if school_type:
        sample = [s for s in sample if s["type"] == school_type.lower()]
    return {"source": "DEMO — verify at nemis.go.ke", "county": county, "level": level,
            "level_description": levels.get(level.lower(), "See nemis.go.ke"),
            "sample_schools": sample, "full_registry": "nemis.go.ke — National Education Management Information System"}

@mcp.tool(name="exam_results_guide", description="Guide to KCPE/KCSE results, grading, and cluster points. DEMO.")
def exam_results_guide(exam: str, concern: Optional[str] = None) -> dict:
    GUIDE = {
        "kcpe": {"full_name": "Kenya Certificate of Primary Education", "marks": "500 total (5 subjects × 100)",
                 "grading": "A–E grades. Grade A = 400+. Used for Form 1 placement.",
                 "results": "Available at knec.ac.ke and via SMS. Released typically in late November.",
                 "placement": "National schools (400+), Extra-county (350+), County schools (300+)"},
        "kcse": {"full_name": "Kenya Certificate of Secondary Education", "grades": "A to E, mean grade used",
                 "grading": "A(12pts) to E(1pt). Mean grade C+ required for university.",
                 "results": "knec.ac.ke. Released November–December.",
                 "cluster_points": "University cluster points: Science (Physics+Chemistry+Math+Bio), Arts (different combos)"},
    }
    exam_key = exam.lower()
    data = GUIDE.get(exam_key, GUIDE["kcse"])
    return {"source": "DEMO — knec.ac.ke for official results", "exam": exam, **data,
            "official": "knec.ac.ke", "university_admissions": "kuccps.net"}

@mcp.tool(name="helb_loan_info", description="HELB loan eligibility, application, and repayment. DEMO.")
def helb_loan_info(query: str, student_type: Optional[str] = "undergraduate") -> dict:
    INFO = {
        "eligibility": "Kenyan citizen, enrolled in accredited university or TVET, not in default.",
        "amounts": "Undergrad: KES 10,000–60,000/year depending on parental income. TVET: KES 8,000–50,000.",
        "application": "Apply at helb.co.ke. Requires: ID, admission letter, KRA PIN, guarantors (2 required).",
        "repayment": "Begins 1 year after graduation. 4% interest. 10–15 year repayment period.",
        "default": "Defaulters listed on CRB. Employers can garnish salary. Must pay before further government services.",
        "bursary": "Separate from loans. Apply via county government or Constituency Development Fund (CDF).",
    }
    q = query.lower()
    matched = {k: v for k, v in INFO.items() if k in q or any(w in q for w in k.split("_"))}
    return {"source": "DEMO — helb.co.ke for official info", "query": query,
            "student_type": student_type, "information": matched or INFO,
            "official": "helb.co.ke", "disclaimer": "Verify all amounts at HELB — rates change annually."}

@mcp.tool(name="tvet_programs", description="TVET programs available in Kenya by trade or county. DEMO.")
def tvet_programs(trade: Optional[str] = None, county: Optional[str] = None) -> dict:
    PROGRAMS = [
        {"trade": "electrical", "nqf_level": 4, "duration": "2 years", "qualification": "Craft Certificate",
         "provider": "National Polytechnic or Accredited TVET"},
        {"trade": "automotive", "nqf_level": 4, "duration": "2 years", "qualification": "Craft Certificate",
         "provider": "Kenya Institute of Highways & Building Technology"},
        {"trade": "ict", "nqf_level": 5, "duration": "3 years", "qualification": "Diploma",
         "provider": "Technical University or accredited TVET"},
        {"trade": "fashion_design", "nqf_level": 4, "duration": "2 years", "qualification": "Craft Certificate",
         "provider": "Kenya Utalii/TVET"},
        {"trade": "plumbing", "nqf_level": 3, "duration": "1 year", "qualification": "Artisan Certificate",
         "provider": "NITA-accredited VTC"},
        {"trade": "agriculture", "nqf_level": 4, "duration": "2 years", "qualification": "Craft Certificate",
         "provider": "Kenya Agricultural TVETs"},
    ]
    if trade:
        PROGRAMS = [p for p in PROGRAMS if trade.lower() in p["trade"]]
    return {"source": "DEMO — tveta.go.ke for full registry", "trade_query": trade, "county": county,
            "programs": PROGRAMS, "accreditation": "tveta.go.ke", "helb": "TVET students eligible for HELB"}

@mcp.tool(name="literacy_resources", description="Adult education, literacy programs, and continuing education in Kenya. DEMO.")
def literacy_resources(county: Optional[str] = None, age_group: Optional[str] = "adult") -> dict:
    return {"source": "DEMO — literacy.go.ke", "county": county, "age_group": age_group,
            "programs": [
                {"name": "Kenya Literacy Programme", "provider": "Ministry of Education", "target": "Adults 15+",
                 "delivery": "Community learning centres", "cost": "Free at public centres"},
                {"name": "Non-Formal Education (NFE)", "provider": "County governments",
                 "target": "Out-of-school youth and adults", "delivery": "Evening/weekend classes"},
                {"name": "Kenya Open Learning Institute (KOLI)", "provider": "Ministry of Education",
                 "target": "Adult distance learners", "delivery": "Distance/blended"},
            ],
            "contact": "County Director of Education for local literacy centre locations."}
