def parse_button_route(data: str):
    # repos:get_repos?user_id=10&token=asdfsadf
    res = {
        'route': {

        },
        'vars': {

        }
    }

    if '?' not in data:
        return None

    routes, vars = data.split("?")
    routes = routes.split(":")
    vars = vars.split("&")

    for index, route in enumerate(routes):
        res['route'][str(index)] = route

    if len(vars[0]) > 0:
        for var in vars:
            name, val = var.split("=")
            res['vars'][name] = val

    return res
