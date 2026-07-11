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

    <div class="card p-3 mt-4 mb-4">

        <h5>Search & Filter</h5>

        <div class="row">

            <div class="col-md-3">

                <input
                    v-model="filters.name"
                    class="form-control"
                    placeholder="Trek Name"
                >

            </div>

            <div class="col-md-3">

                <input
                    v-model="filters.location"
                    class="form-control"
                    placeholder="Location"
                >

            </div>

            <div class="col-md-2">

                <select
                    v-model="filters.difficulty"
                    class="form-select"
                >

                    <option value="">Difficulty</option>

                    <option>Easy</option>

                    <option>Moderate</option>

                    <option>Hard</option>

                </select>

            </div>

            <div class="col-md-2">

                <input
                    type="number"
                    v-model="filters.duration"
                    class="form-control"
                    placeholder="Duration"
                >

            </div>

            <div class="col-md-2">

                <button
                    class="btn btn-primary me-2"
                    @click="loadTreks"
                >
                    Search
                </button>

                <button
                    class="btn btn-secondary"
                    @click="clearFilters"
                >
                    Clear
                </button>

            </div>

        </div>

    </div>

    <table class="table table-bordered table-striped">

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

const filters = ref({

    name: "",

    location: "",

    difficulty: "",

    duration: ""

})

async function loadTreks() {

    const response = await api.get(

        "/trekker/treks",

        {

            params: {

                name: filters.value.name,

                location: filters.value.location,

                difficulty: filters.value.difficulty,

                duration: filters.value.duration

            }

        }

    )

    treks.value = response.data

}

function clearFilters() {

    filters.value = {

        name: "",

        location: "",

        difficulty: "",

        duration: ""

    }

    loadTreks()

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