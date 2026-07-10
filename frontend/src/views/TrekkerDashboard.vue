<template>

<div class="container mt-5">

    <div class="d-flex justify-content-between align-items-center mb-4">

        <h2>Welcome {{ name }}</h2>

        <button
            class="btn btn-danger"
            @click="logout"
        >
            Logout
        </button>

    </div>

    <div class="mb-4">

        <router-link
            to="/trekker/treks"
            class="btn btn-primary me-2"
        >
            Browse Treks
        </router-link>

        <router-link
            to="/trekker/bookings"
            class="btn btn-success me-2"
        >
            My Bookings
        </router-link>

        <router-link
            to="/trekker/profile"
            class="btn btn-success"
        >
            Profile
        </router-link>


    </div>

    <hr>

    <div class="row">

        <div class="col-md-4">

            <div class="card p-3">

                <h5>Available Treks</h5>

                <h3>{{ dashboard.available_treks }}</h3>

            </div>

        </div>

        <div class="col-md-4">

            <div class="card p-3">

                <h5>My Bookings</h5>

                <h3>{{ dashboard.my_bookings }}</h3>

            </div>

        </div>

        <div class="col-md-4">

            <div class="card p-3">

                <h5>Completed Treks</h5>

                <h3>{{ dashboard.completed_treks }}</h3>

            </div>

        </div>

    </div>

</div>

</template>

<script setup>

import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"

import api from "../services/api"

const router = useRouter()

const dashboard = ref({})

const name = localStorage.getItem("name")

async function loadDashboard() {

    const response = await api.get("/trekker/dashboard")

    dashboard.value = response.data

}

function logout() {

    localStorage.clear()

    router.push("/")

}

onMounted(() => {

    loadDashboard()

})

</script>