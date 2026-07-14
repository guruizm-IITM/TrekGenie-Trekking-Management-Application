<template>

<div class="container mt-5">

    <div class="d-flex justify-content-between align-items-center mb-4">

        <div class="d-flex align-items-center">

            <img
                src="../assets/logo-icon.png"
                class="admin-logo me-3"
                alt="TrekGenie"
            >

            <div>

                <h3 class="mb-0">

                    Welcome, {{ name }}

                </h3>

                <small class="text-muted">

                    Administrator Portal

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

    <div class="mb-4">

        <router-link
            to="/admin/staff"
            class="btn btn-primary me-2"
        >
            Manage Staff
        </router-link>

        <router-link
            to="/admin/treks"
            class="btn btn-success me-2"
        >
            Manage Treks
        </router-link>

        <router-link
            to="/admin/users"
            class="btn btn-warning me-2"
        >
            View Users
        </router-link>

        <router-link
            to="/admin/bookings"
            class="btn btn-info"
        >
            View Bookings
        </router-link>

    </div>

    <hr>

    <div class="row">

        <div class="col-md-4">

            <div class="card p-3">

                <h5>Total Treks</h5>

                <h3>{{ dashboard.total_treks }}</h3>

            </div>

        </div>

        <div class="col-md-4">

            <div class="card p-3">

                <h5>Total Staff</h5>

                <h3>{{ dashboard.total_staff }}</h3>

            </div>

        </div>

        <div class="col-md-4">

            <div class="card p-3">

                <h5>Total Bookings</h5>

                <h3>{{ dashboard.total_bookings }}</h3>

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

onMounted(async () => {

    const response = await api.get("/admin/dashboard")

    dashboard.value = response.data

})

function logout() {

    localStorage.clear()

    router.push("/")

}

</script>

<style scoped>

.admin-logo{

    width:75px;

    height:auto;

}

</style>

