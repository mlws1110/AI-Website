import json
from app import create_app, db
from app.models.tool import Tool

def update_tool_websites():
    app = create_app()
    app.app_context().push()

    # Load tool-website mappings from JSON file
    with open('tools_websites.json', 'r') as file:
        tools_with_websites = json.load(file)

    updated_count = 0
    not_found = []

    for tool_name, website_url in tools_with_websites.items():
        tool = Tool.query.filter_by(name=tool_name).first()

        if tool:
            tool.website = website_url
            updated_count += 1
            print(f"Updated '{tool.name}' with website: {tool.website}")
        else:
            not_found.append(tool_name)
            print(f"Tool '{tool_name}' not found in the database.")

    if updated_count > 0:
        db.session.commit()
        print(f"\nSuccessfully updated {updated_count} tool(s).")
    else:
        print("\nNo tools were updated.")

    if not_found:
        print("\nThe following tools were not found and were not updated:")
        for name in not_found:
            print(f"- {name}")

if __name__ == "__main__":
    update_tool_websites()