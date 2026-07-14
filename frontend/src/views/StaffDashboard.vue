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

                    Staff Portal

                </small>

            </div>

        </div>

        <button
            class="btn btn-danger"
            @click="logout"
        >
            Logout
        </button>

    </div>

    <p class="text-muted mb-4">

        View your assigned treks and manage trekking activities.

    </p>

    <div class="d-flex flex-wrap gap-2 mb-4">

        <router-link
            to="/staff/treks"
            class="btn btn-success"
        >
            🏔 My Treks
        </router-link>

    </div>

    <hr>

    <div class="row g-4">

        <div class="col-md-4">

            <div class="card shadow-sm text-center p-4 h-100">

                <h5>Assigned Treks</h5>

                <h2 class="text-primary fw-bold">

                    {{ dashboard.assigned_treks }}

                </h2>

            </div>

        </div>

        <div class="col-md-4">

            <div class="card shadow-sm text-center p-4 h-100">

                <h5>Active Treks</h5>

                <h2 class="text-success fw-bold">

                    {{ dashboard.active_treks }}

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

    const response = await api.get("/staff/dashboard")

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

<style scoped>

.dashboard-logo{

    width:70px;

    height:auto;

}

</style>