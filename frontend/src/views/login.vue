<template>

<div class="login-page">

    <div class="login-card">

        <div class="text-center mb-4">

            <img
                src="../assets/logo.png"
                alt="TrekGenie"
                class="logo"
            >

            <h1 class="brand-title">

                Trek<span class="brand-green">Genie</span>

            </h1>

            <p class="brand-subtitle">

                Adventure Begins Here.

            </p>

        </div>

        <form @submit.prevent="login">

            <div class="mb-3">

                <input
                    v-model="email"
                    type="email"
                    class="form-control custom-input"
                    placeholder="Email Address"
                >

            </div>

            <div class="mb-3">

                <input
                    type="password"
                    v-model="password"
                    class="form-control custom-input"
                    placeholder="Password"
                >

            </div>

            <div
                v-if="message"
                class="alert alert-danger"
            >

                {{ message }}

            </div>

            <button
                type="submit"
                class="btn btn-success login-btn"
            >

                Login →

            </button>

        </form>

    </div>

    <div class="footer">

        © 2026 TrekGenie

        <br>

        Explore • Experience • Excel

    </div>

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

async function login() {

    try {

        const response = await api.post(
            "/auth/login",
            {
                email: email.value,
                password: password.value
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

<style scoped>

.login-page{

    min-height:100vh;

    display:flex;

    justify-content:center;

    align-items:center;

    background:url("/src/assets/login-bg.png");

    background-size:cover;

    background-position:center;

    background-repeat:no-repeat;

    position:relative;

}

.login-page::before{

    content:"";

    position:absolute;

    inset:0;

    background:rgba(0,0,0,.28);

}

.login-card{

    position:relative;

    z-index:1;

    width:420px;

    background:rgba(255,255,255,.96);

    backdrop-filter:blur(10px);

    border-radius:20px;

    padding:35px 40px;

    box-shadow:0 18px 45px rgba(0,0,0,.25);

}

.logo{

    width:180px;

    height:auto;

    display:block;

    margin:0 auto;

}

.brand-title{

    font-size:2.6rem;

    font-weight:700;

    color:#333333;

    margin-top:12px;

    margin-bottom:4px;

}

.brand-green{

    color:#2E7D32;

}

.brand-subtitle{

    color:#6c757d;

    font-size:.95rem;

    letter-spacing:2px;

    text-transform:uppercase;

    margin-bottom:28px;

}

.custom-input{

    height:54px;

    border-radius:12px;

    font-size:1rem;

}

.login-btn{

    width:100%;

    height:54px;

    border-radius:12px;

    font-size:1.05rem;

    font-weight:600;

    margin-top:10px;

}

.footer{

    position:absolute;

    bottom:25px;

    width:100%;

    text-align:center;

    color:white;

    font-size:.9rem;

    z-index:2;

    text-shadow:0 2px 6px rgba(0,0,0,.5);

}

</style>