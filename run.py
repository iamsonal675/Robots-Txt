import pandas as pd
import re

def parse_robots_txt(robots_txt):
    rules = {'User-agent': [], 'Allow': [], 'Disallow': []}
    current_user_agent = None

    for line in robots_txt.splitlines():
        line = line.strip()
        if line.startswith("User-agent:"):
            current_user_agent = line.split("User-agent:")[1].strip()
            rules['User-agent'].append(current_user_agent)
        elif line.startswith("Allow:"):
            path = line.split("Allow:")[1].strip()
            rules['Allow'].append((current_user_agent, path))
        elif line.startswith("Disallow:"):
            path = line.split("Disallow:")[1].strip()
            rules['Disallow'].append((current_user_agent, path))
    
    return rules

def save_rules_to_csv(rules, allow_filename, disallow_filename):
    allow_df = pd.DataFrame(rules['Allow'], columns=['User-agent', 'Path'])
    disallow_df = pd.DataFrame(rules['Disallow'], columns=['User-agent', 'Path'])
    
    allow_df.to_csv(allow_filename, index=False)
    disallow_df.to_csv(disallow_filename, index=False)

def main():
     with open("./robots.txt","r") as f:
          robots_txt = f.read()
          rules = parse_robots_txt(robots_txt)
          save_rules_to_csv(rules, "allow_rules.csv", "disallow_rules.csv")

if __name__ == "__main__":
    main()
