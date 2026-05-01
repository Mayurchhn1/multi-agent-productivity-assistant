# -----------------------------
# 🧠 DECISION ENGINE
# -----------------------------

from app.db.database import fetch_active_deals_from_db


def get_context(limit: int = 5):
    deals = fetch_active_deals_from_db(limit=50)

    # -----------------------------
    # 🔥 SIMPLE DEAL RANKING
    # -----------------------------
    sorted_deals = sorted(
        deals,
        key=lambda x: x.get("value", 0),
        reverse=True
    )

    top_deals = sorted_deals[:limit]

    # -----------------------------
    # 📊 PIPELINE SUMMARY
    # -----------------------------
    total_value = sum(d.get("value", 0) for d in deals)

    pipeline = {
        "total_deals": len(deals),
        "total_value": total_value
    }

    return {
        "top_deals": top_deals,
        "pipeline": pipeline
    }
