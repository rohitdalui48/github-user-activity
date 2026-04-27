import argparse
import requests
import sys
import tabulate
from typing import List, Dict, Optional, TypedDict


def get_github_username() -> str:
    parser = argparse.ArgumentParser(description="Github User activiry tracker")
    parser.add_argument("username", type=str)
    args = parser.parse_args()
    return args.username


def get_user_activity(username: str) -> Optional[List[Dict]]:
    try:
        response = requests.get(
            f"https://api.github.com/users/{username}/events", timeout=1
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.ConnectionError:
        print("Network Issue")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error\n{e}")

    except requests.exceptions.Timeout:
        print("Server Timeout")

    except requests.exceptions.InvalidURL:
        print("Invalid Username")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


class Data(TypedDict):
    repos: List[str]
    counts: List[int]


def format_data(activities: List[Dict]) -> Dict:
    formatted_data = {}
    for activity in activities:
        activity_type = activity["type"]
        activity_repo = activity["repo"]["name"]
        if activity_type not in formatted_data.keys():
            formatted_data[f"{activity_type}"] = {
                "repos": [activity_repo],
                "counts": [1],
            }

        else:
            if activity_repo not in formatted_data[f"{ activity_type }"]["repos"]:
                formatted_data[f"{ activity_type }"]["repos"].append(
                    f"{ activity_repo }"
                )
                formatted_data[f"{ activity_type }"]["counts"].append(1)
            else:
                index = formatted_data[f"{activity_type}"]["repos"].index(
                    f"{ activity_repo }"
                )
                formatted_data[f"{activity_type}"]["counts"][index] += 1
    return formatted_data


def show_activity(data: Data) -> None:
    show_data = []
    for activity in data.keys():
        show_data.append([
            activity,
            "\n".join(repo for repo in data[f"{activity}"]["repos"]),
            "\n".join(str(count) for count in data[f"{activity}"]["counts"])
        ])

    print(tabulate.tabulate(show_data,["Action", "Repo", "Count"], tablefmt="grid"))


def main():
    github_username: str = get_github_username()
    user_activity: Optional[List[Dict]] = get_user_activity(github_username)
    if (user_activity) is None :
        print("Try Again Later")
        sys.exit()
    else:
        formatted_data = format_data(user_activity)
        show_activity(formatted_data)


if __name__ == "__main__":
    main()
