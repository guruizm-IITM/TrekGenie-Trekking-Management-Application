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
            to="/staff/treks"
            class="btn btn-primary"
        >
            My Treks
        </router-link>

    </div>

    <hr>

    <div class="row">

        <div class="col-md-4">

            <div class="card p-3">

                <h5>Assigned Treks</h5>

                <h3>{{ dashboard.assigned_treks }}</h3>

            </div>

        </div>

        <div class="col-md-4">

            <div class="card p-3">

                <h5>Active Treks</h5>

                <h3>{{ dashboard.active_treks }}</h3>

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