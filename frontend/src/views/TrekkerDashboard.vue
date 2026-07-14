<template>

<div class="container mt-5">

    <div class="d-flex justify-content-between align-items-center mb-4">

        <div class="d-flex align-items-center">

            <img
                src="../assets/logo-icon.png"
                class="dashboard-logo me-3"
                alt="TrekGenie"
            >

            <div>

                <h3 class="mb-0">

                    Welcome, {{ name }}

                </h3>

                <small class="text-muted">

                    Explorer Dashboard

                </small>

            </div>

        </div>

        <button
            class="btn btn-danger"
            @click="logout"
        >
            Sign Out
        </button>

    </div>

    <p class="text-muted mb-4">

        Browse exciting trekking adventures, manage your bookings and keep your profile up to date.

    </p>

    <div class="d-flex flex-wrap gap-2 mb-4">

        <router-link
            to="/trekker/treks"
            class="btn btn-success"
        >
            🏔 Browse Treks
        </router-link>

        <router-link
            to="/trekker/bookings"
            class="btn btn-primary"
        >
            📋 My Bookings
        </router-link>

        <router-link
            to="/trekker/profile"
            class="btn btn-secondary"
        >
            👤 Profile
        </router-link>

        <button
            class="btn btn-warning"
            @click="exportHistory"
        >
            📥 Export Booking History
        </button>

    </div>

    <hr>

    <div class="row g-4">

        <div class="col-md-4">

            <div class="card shadow-sm text-center p-4 h-100">

                <h5>Available Treks</h5>

                <h2 class="text-success fw-bold">

                    {{ dashboard.available_treks }}

                </h2>

            </div>

        </div>

        <div class="col-md-4">

            <div class="card shadow-sm text-center p-4 h-100">

                <h5>My Bookings</h5>

                <h2 class="text-primary fw-bold">

                    {{ dashboard.my_bookings }}

                </h2>

            </div>

        </div>

        <div class="col-md-4">

            <div class="card shadow-sm text-center p-4 h-100">

                <h5>Completed Treks</h5>

                <h2 class="text-secondary fw-bold">

                    {{ dashboard.completed_treks }}

                </h2>

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

async function exportHistory() {

    const response = await api.post(
        "/trekker/export"
    )

    alert(response.data.message)

}

function logout() {

    localStorage.clear()

    router.push("/")

}

onMounted(() => {

    loadDashboard()

})

</script>

<style scoped>

.dashboard-logo{

    width:70px;

    height:auto;

}

</style>