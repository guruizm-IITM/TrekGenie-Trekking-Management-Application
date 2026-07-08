export function getToken() {

    return localStorage.getItem("token")

}

export function getRole() {

    return localStorage.getItem("role")

}

export function getName() {

    return localStorage.getItem("name")

}

export function logout() {

    localStorage.clear()

}