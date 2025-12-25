# examples/sample_integration.py

from sdk.astraforge_client import AstroFrogeClient

# Initialize the AstroFroge client
astro = AstroFrogeClient(config_path="astraforge_config.yaml")

# 1️⃣ Generate AI-based test plan
astro.generate_test_plan(requirements="user_login_module")

# 2️⃣ Auto-detect UI elements
astro.deep_scan_ui(url="https://demo.testapp.com/login")

# 3️⃣ Execute tests with preferred executor
astro.run_tests(executor="cypress_executor")

# 4️⃣ Collect and analyze results
astro.generate_report(output="reports/dashboard.html")

print("✅ Test execution complete. Reports saved in /reports.")
