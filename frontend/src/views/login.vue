<template>

<div class="container mt-5">

    <h2>Login</h2>

    <div class="mb-3">

        <input
            v-model="email"
            class="form-control"
            placeholder="Email"
        >

    </div>

    <div class="mb-3">

        <input
            type="password"
            v-model="password"
            class="form-control"
            placeholder="Password"
        >

    </div>

    <div v-if="message" class="alert alert-danger mt-3">

    {{ message }}

    </div>

    <button
        class="btn btn-primary"
        @click="login"
    >
        Login
    </button>

</div>

</template>

<script setup>

import { ref } from "vue"

import { useRouter } from "vue-router"

import api from "../services/api"

const email = ref("")
const password = ref("")
const message = ref("")

const router = useRouter()

async function login(){

    try{

        const response = await api.post(

            "/auth/login",

            {

                email:email.value,

                password:password.value

            }

        )

        localStorage.setItem(
            "token",
            response.data.access_token
        )

        localStorage.setItem(
            "role",
            response.data.role
        )

        localStorage.setItem(
            "name",
            response.data.user
        )

        if (response.data.role === "admin") {

            router.push("/admin")

        }
        else if (response.data.role === "staff") {

            router.push("/staff")

        }
        else {

            router.push("/trekker")

        }

    }

    catch (error) {

        if (error.response) {

            message.value = error.response.data.message

        }

        else {

            message.value = "Unable to connect to the server."

        }

    }

}

</script>