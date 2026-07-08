<template>

<div class="container mt-5">

    <div class="d-flex justify-content-between align-items-center mb-4">

        <button
            class="btn btn-outline-secondary"
            @click="router.push('/admin')"
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

    <h2>Trek Management</h2>

    <div class="card p-4 mb-4">

        <h4>Create Trek</h4>

        <input
            v-model="form.name"
            class="form-control mb-2"
            placeholder="Trek Name"
        >

        <input
            v-model="form.location"
            class="form-control mb-2"
            placeholder="Location"
        >

        <textarea
            v-model="form.description"
            class="form-control mb-2"
            placeholder="Description"
        ></textarea>

        <select
            v-model="form.difficulty"
            class="form-select mb-2"
        >
            <option>Easy</option>
            <option>Moderate</option>
            <option>Hard</option>
        </select>

        <input
            type="number"
            v-model="form.duration"
            class="form-control mb-2"
            placeholder="Duration (Days)"
        >

        <input
            type="number"
            v-model="form.available_slots"
            class="form-control mb-2"
            placeholder="Available Slots"
        >

        <input
            type="date"
            v-model="form.start_date"
            class="form-control mb-2"
        >

        <input
            type="date"
            v-model="form.end_date"
            class="form-control mb-3"
        >

        <button
            class="btn btn-success"
            @click="createTrek"
        >
            Create Trek
        </button>

    </div>

    <table class="table table-bordered table-striped">

        <thead>

            <tr>

                <th>ID</th>
                <th>Name</th>
                <th>Location</th>
                <th>Difficulty</th>
                <th>Slots</th>
                <th>Status</th>
                <th>Assigned Staff</th>
                <th>Assign Staff</th>
                <th>Action</th>

            </tr>

        </thead>

        <tbody>

            <tr
                v-for="trek in trekList"
                :key="trek.id"
            >

                <td>{{ trek.id }}</td>

                <td>{{ trek.name }}</td>

                <td>{{ trek.location }}</td>

                <td>{{ trek.difficulty }}</td>

                <td>{{ trek.available_slots }}</td>

                <td>{{ trek.status }}</td>

                <td>{{ trek.assigned_staff }}</td>

                <td>

                    <select
                        class="form-select"
                        v-model="trek.selectedStaff"
                    >

                        <option value="">
                            Select Staff
                        </option>

                        <option
                            v-for="staff in staffList"
                            :key="staff.id"
                            :value="staff.id"
                        >

                            {{ staff.name }}

                        </option>

                    </select>

                </td>

                <td>

                    <button
                        class="btn btn-primary btn-sm"
                        @click="assignStaff(trek)"
                    >
                        Assign
                    </button>

                </td>

            </tr>

        </tbody>

    </table>

</div>

</template>

<script setup>

import { useRouter } from "vue-router"

import { ref, onMounted } from "vue"

import api from "../services/api"

const trekList = ref([])

const staffList = ref([])

const form = ref({

    name: "",

    location: "",

    description: "",

    difficulty: "Easy",

    duration: "",

    available_slots: "",

    start_date: "",

    end_date: ""

})

const router = useRouter()

async function loadTreks() {

    try {

        const response = await api.get("/admin/treks")

        trekList.value = response.data.map(trek => ({

            ...trek,

            selectedStaff: ""

        }))

    }

    catch (error) {

        console.log(error)

    }

}

async function loadStaff() {

    try {

        const response = await api.get("/admin/staff")

        staffList.value = response.data.filter(

            staff => staff.active

        )

    }

    catch (error) {

        console.log(error)

    }

}

async function createTrek() {

    try {

        await api.post("/admin/treks", form.value)

        form.value = {

            name: "",

            location: "",

            description: "",

            difficulty: "Easy",

            duration: "",

            available_slots: "",

            start_date: "",

            end_date: ""

        }

        loadTreks()

    }

    catch (error) {

        console.log(error)

    }

}

async function assignStaff(trek) {

    if (!trek.selectedStaff) {

        alert("Please select a staff member.")

        return

    }

    try {

        await api.patch(

            `/admin/treks/${trek.id}/assign`,

            {

                staff_id: trek.selectedStaff

            }

        )

        alert("Staff assigned successfully.")

        loadTreks()

    }

    catch (error) {

        console.log(error)

    }

}

function logout() {

    localStorage.clear()

    router.push("/")

}

onMounted(() => {

    loadTreks()

    loadStaff()

})

</script>