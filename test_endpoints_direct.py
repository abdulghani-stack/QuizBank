import app
import json

client = app.app.test_client()

# 1. Health
res_health = client.get('/health')
print(f"GET /health: status={res_health.status_code}, data={res_health.json}")
assert res_health.status_code == 200

# 2. Items
res_items = client.get('/items')
print(f"GET /items: status={res_items.status_code}, count={len(res_items.json)}")
assert res_items.status_code == 200
assert len(res_items.json) == 420

# 3. Study Material
res_study = client.get('/api/study-material')
print(f"GET /api/study-material: status={res_study.status_code}, count={len(res_study.json)}")
assert res_study.status_code == 200
assert len(res_study.json) == 7

# 4. Study Material Detail
res_detail = client.get('/api/study-material/2015111')
print(f"GET /api/study-material/2015111: status={res_detail.status_code}, title={res_detail.json.get('subject')}")
assert res_detail.status_code == 200

# 5. Syllabus
res_syl = client.get('/api/syllabus')
print(f"GET /api/syllabus: status={res_syl.status_code}, subjects={len(res_syl.json.get('subjects'))}")
assert res_syl.status_code == 200

# 6. Metrics
res_met = client.get('/metrics')
print(f"GET /metrics: status={res_met.status_code}, len={len(res_met.data)}")
assert res_met.status_code == 200

print("\nAll Backend Endpoints are 100% OPERATIONAL!")
