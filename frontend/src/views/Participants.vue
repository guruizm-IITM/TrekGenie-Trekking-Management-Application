<template>

<div class="container mt-5">

    <div class="d-flex justify-content-between align-items-center mb-4">

        <button
            class="btn btn-outline-secondary"
            @click="router.push('/staff/treks')"
        >
            ← My Treks
        </button>

        <button
            class="btn btn-danger"
            @click="logout"
        >
            Logout
        </button>

    </div>

    <h2>Participants</h2>

    <h5 class="mb-4">{{ trekName }}</h5>

    <table class="table table-bordered table-striped">

        <thead>

            <tr>

                <th>Booking ID</th>

                <th>Name</th>

                <th>Email</th>

                <th>Booking Status</th>

                <th>Payment Status</th>

            </tr>

        </thead>

        <tbody>

            <tr
                v-for="participant in participants"
                :key="participant.booking_id"
            >

                <td>{{ participant.booking_id }}</td>

                <td>{{ participant.name }}</td>

                <td>{{ participant.email }}</td>

                <td>{{ participant.booking_status }}</td>

                <td>{{ participant.payment_status }}</td>

            </tr>

        </tbody>

    </table>

</div>

</template>

<script setup>

import { ref, onMounted } from "vue"

import { useRouter, useRoute } from "vue-router"

import api from "../services/api"

const router = useRouter()

const route = useRoute()

const trekName = ref("")

const participants = ref([])

async function loadParticipants() {

    const response = await api.get(

        `/staff/treks/${route.params.trekId}/participants`

    )

    trekName.value = response.data.trek_name

    participants.value = response.data.participants

}

function logout() {

    localStorage.clear()

    router.push("/")

}

onMounted(() => {

    loadParticipants()

})

</script>