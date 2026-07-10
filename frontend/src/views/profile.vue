<template>

<div class="container mt-5">

    <div class="d-flex justify-content-between align-items-center mb-4">

        <button
            class="btn btn-outline-secondary"
            @click="router.push('/trekker')"
        >
            ← Dashboard
        </button>

        <button
            class="btn btn-danger"
            @click="logout"
        >
            Logout
        </button>

    </div>

    <h2>My Profile</h2>

    <form
        class="mt-4"
        @submit.prevent="saveProfile"
    >

        <div class="mb-3">

            <label class="form-label">Name</label>

            <input
                v-model="profile.name"
                class="form-control"
                required
            >

        </div>

        <div class="mb-3">

            <label class="form-label">Email</label>

            <input
                v-model="profile.email"
                class="form-control"
                disabled
            >

        </div>

        <div class="mb-3">

            <label class="form-label">Phone</label>

            <input
                v-model="profile.phone"
                class="form-control"
                required
            >

        </div>

        <button
            type="submit"
            class="btn btn-primary"
        >
            Save Changes
        </button>

    </form>

</div>

</template>

<script setup>

import { ref, onMounted } from "vue"

import { useRouter } from "vue-router"

import api from "../services/api"

const router = useRouter()

const profile = ref({})

async function loadProfile() {

    const response = await api.get("/trekker/profile")

    profile.value = response.data

}

async function saveProfile() {

    await api.patch(

        "/trekker/profile",

        {

            name: profile.value.name,

            phone: profile.value.phone

        }

    )

    alert("Profile updated successfully.")

}

function logout() {

    localStorage.clear()

    router.push("/")

}

onMounted(() => {

    loadProfile()

})

</script>