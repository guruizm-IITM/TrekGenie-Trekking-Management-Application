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

    <h2>Available Treks</h2>

    <table class="table table-bordered table-striped mt-4">

        <thead>

            <tr>

                <th>Name</th>

                <th>Location</th>

                <th>Difficulty</th>

                <th>Duration</th>

                <th>Slots</th>

                <th>Start</th>

                <th>End</th>

                <th>Action</th>

            </tr>

        </thead>

        <tbody>

            <tr
                v-for="trek in treks"
                :key="trek.id"
            >

                <td>{{ trek.name }}</td>

                <td>{{ trek.location }}</td>

                <td>{{ trek.difficulty }}</td>

                <td>{{ trek.duration }} Days</td>

                <td>{{ trek.available_slots }}</td>

                <td>{{ trek.start_date }}</td>

                <td>{{ trek.end_date }}</td>

                <td>

                    <button
                        class="btn btn-success btn-sm"
                        @click="bookTrek(trek.id)"
                    >
                        Book
                    </button>

                </td>

            </tr>

        </tbody>

    </table>

</div>

</template>

<script setup>

import { ref, onMounted } from "vue"

import { useRouter } from "vue-router"

import api from "../services/api"

const router = useRouter()

const treks = ref([])

async function loadTreks() {

    const response = await api.get("/trekker/treks")

    treks.value = response.data

}

async function bookTrek(id) {

    try {

        await api.post(

            "/trekker/bookings",

            {

                trek_id: id

            }

        )

        alert("Trek booked successfully.")

        loadTreks()

    }

    catch(error) {

        alert(error.response.data.message)

    }

}

function logout() {

    localStorage.clear()

    router.push("/")

}

onMounted(() => {

    loadTreks()

})

</script>