import requests

def call():

    condition = True

    while condition == True:
        ip = input("Please enter your ip address: ")    
        url = f"http://{ip}/api/auth"
        password = input("Please enter your password: ")
        try:
            response = requests.post(url, json={"password": password})
            sid = response.json()["session"]["sid"]

            stats_url = f"http://{ip}/api/stats/summary"
            headers = {"X-FTL-SID": sid}
            stats_response = requests.get(stats_url, headers=headers)
            info = stats_response.json()
            condition = False
    

        except:
            print("Ip address or password was incorrect, please try again...")
            condition = True


    queries_today = info["queries"]["total"]
    queries_blocked = info["queries"]["blocked"]
    percent_blocked = info["queries"]["percent_blocked"]
    domains_blocked = info["gravity"]["domains_being_blocked"]
    return queries_today, queries_blocked, percent_blocked, domains_blocked
    
call()
