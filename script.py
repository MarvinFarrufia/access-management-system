# ==========================================================
# Project: Access Management System (AMS)
# Client: Local Business
# Description: Generates an authorized user report
#              for the primary terminal.
# Phase: 1.0 (Initial Release)
# ==========================================================

# Inventory of assets (Terminals)
main_machines = ["pc00598"]

# Register of authorized employees
authorized_users = [
    'cardona_25',
    'h_farrufia',
    'j_valencia',
    "user_01"
]

# Report generation process
for machine in main_machines:
    for user in authorized_users:
        print(f"The user {user} is authorized to work on terminal: {machine}")