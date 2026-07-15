import axios from "axios";

const api = axios.create({

    baseURL: "http://127.0.0.1:5000"

});

api.interceptors.request.use(

    (config) => {

        const token = localStorage.getItem("token");

        if (token) {

            config.headers.Authorization = `Bearer ${token}`;

        }

        return config;

    }

);

api.interceptors.response.use(

    response => response,

    error => {

        if (

            localStorage.getItem("token") &&

            [401,422].includes(error.response?.status)

        ) {

            localStorage.clear();

            alert("Your session has expired. Please login again.");

            window.location.replace("/");

        }

        return Promise.reject(error);

    }

);

export default api;