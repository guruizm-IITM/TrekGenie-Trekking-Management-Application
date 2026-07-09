<template>

<div class="container mt-5">

    <div class="d-flex justify-content-between align-items-center mb-4">

        <button
            class="btn btn-outline-secondary"
            @click="router.push('/staff')"
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

    <h2>My Treks</h2>

    <table class="table table-bordered table-striped mt-4">

        <thead>

            <tr>

                <th>Name</th>

                <th>Location</th>

                <th>Status</th>

                <th>Slots</th>

                <th>Update Status</th>

                <th>Update Slots</th>

                <th>Participants</th>

            </tr>

        </thead>

        <tbody>

            <tr
                v-for="trek in treks"
                :key="trek.id"
            >

                <td>{{ trek.name }}</td>

                <td>{{ trek.location }}</td>

                <td>{{ trek.status }}</td>

                <td>{{ trek.available_slots }}</td>

                <td>

                    <select
                        class="form-select"
                        v-model="trek.newStatus"
                    >

                        <option>Open</option>
                        <option>Closed</option>
                        <option>Completed</option>

                    </select>

                    <button
                        class="btn btn-primary btn-sm mt-2"
                        @click="updateStatus(trek)"
                    >
                        Save
                    </button>

                </td>

                <td>

                    <input
                        type="number"
                        class="form-control"
                        v-model="trek.newSlots"
                    >

                    <button
                        class="btn btn-success btn-sm mt-2"
                        @click="updateSlots(trek)"
                    >
                        Save
                    </button>

                </td>

                <td>

                    <button
                        class="btn btn-secondary btn-sm"
                        @click="viewParticipants(trek.id)"
                    >
                        View
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

    const response = await api.get("/staff/treks")

    treks.value = response.data.map(trek => ({

        ...trek,

        newStatus: trek.status,

        newSlots: trek.available_slots

    }))

}

async function updateStatus(trek) {

    try {

        await api.patch(

            `/staff/treks/${trek.id}/status`,

            {

                status: trek.newStatus

            }

        )

        alert("Status updated successfully.")

        loadTreks()

    }

    catch(error) {

        alert(error.response.data.message)

    }

}

async function updateSlots(trek) {

    try {

        await api.patch(

            `/staff/treks/${trek.id}/slots`,

            {

                available_slots: Number(trek.newSlots)

            }

        )

        alert("Available slots updated successfully.")

        loadTreks()

    }

    catch(error) {

        alert(error.response.data.message)

    }

}

function viewParticipants(id) {

    router.push(`/staff/treks/${id}/participants`)

}

function logout() {

    localStorage.clear()

    router.push("/")

}

onMounted(() => {

    loadTreks()

})

</script>