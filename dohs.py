import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 8))

# Define function to add text boxes
def add_box(ax, text, xy, width, height, boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightgrey', fontsize=10):
    box = patches.FancyBboxPatch(xy, width, height, boxstyle=boxstyle, edgecolor=edgecolor, facecolor=facecolor)
    ax.add_patch(box)
    cx = xy[0] + width/2.0
    cy = xy[1] + height/2.0
    ax.text(cx, cy, text, ha='center', va='center', fontsize=fontsize)

# Hide the axes
ax.axis('off')

# Define positions
positions = {
    "clients": (1, 5),
    "api_gateway": (4, 5),
    "load_balancer": (7, 5),
    "on_prem_vpc": (10, 2),
    "cloud_services": (10, 6),
    "backup_systems": (13, 5)
}

# Add boxes for Clients
clients = ["Stakeholders", "Field Workers", "Non-Professionals", "Surveillance"]
for i, client in enumerate(clients):
    add_box(ax, client, (positions["clients"][0], positions["clients"][1] - i), 2, 1)

# Add box for API Gateway
add_box(ax, "API Gateway", positions["api_gateway"], 2, 1)

# Add box for Load Balancer
add_box(ax, "Elastic Load Balancer", positions["load_balancer"], 2, 1)

# Add On-Premises VPC section
on_prem_services = [
    "Auth Services (EC2, RDS)", "Visualization Dashboard (EC2, DynamoDB)", 
    "Alerts/Reports (EC2, DynamoDB)", "Data Analytics (EC2, Redshift)", 
    "Case Management (EC2, RDS)", "Report Generation (EC2, RDS)", 
    "Stakeholder Portal (EC2, RDS)"
]
for i, service in enumerate(on_prem_services):
    add_box(ax, service, (positions["on_prem_vpc"][0], positions["on_prem_vpc"][1] - i), 3, 1)

# Add Cloud Services section
cloud_services = [
    "AI Model Management (SageMaker, DynamoDB)", "AI Inference (Lambda, DynamoDB)", 
    "Public Reporting (EC2, RDS)", "External Data Feeds (EC2, RDS)", 
    "Satellite Channel (Kinesis, DynamoDB)", "Map/GIS Service (EC2, S3)", 
    "Chatbot Service (Lex, DynamoDB)"
]
for i, service in enumerate(cloud_services):
    add_box(ax, service, (positions["cloud_services"][0], positions["cloud_services"][1] - i), 3, 1)

# Add Backup Systems section
backup_systems = [
    "On-Premise Backup (RDS, DynamoDB)", "Cloud Backup (S3, RDS, DynamoDB)", 
    "Data Migration (DMS, DataSync)"
]
for i, system in enumerate(backup_systems):
    add_box(ax, system, (positions["backup_systems"][0], positions["backup_systems"][1] - i), 3, 1)

# Draw connections
connections = [
    (positions["clients"], positions["api_gateway"]),
    (positions["api_gateway"], positions["load_balancer"]),
    (positions["load_balancer"], positions["on_prem_vpc"]),
    (positions["load_balancer"], positions["cloud_services"]),
    (positions["on_prem_vpc"], positions["backup_systems"]),
    (positions["cloud_services"], positions["backup_systems"])
]

for start, end in connections:
    ax.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="->", color='blue'))

plt.show()