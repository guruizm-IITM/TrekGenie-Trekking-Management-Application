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

    <div
        v-if="editingId"
        class="alert alert-warning"
    >

        You are editing an existing trek.

    </div>

    <div class="card p-4 mb-4">

        <h4>{{ editingId ? "Edit Trek" : "Create Trek" }}</h4>

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

            {{ editingId ? "Update Trek" : "Create Trek" }}

        </button>

        <button
            v-if="editingId"
            class="btn btn-secondary ms-2"
            @click="cancelEdit"
        >

            Cancel

        </button>

    </div>

    <div class="row mb-3">

        <div class="col-md-5">

            <input
                v-model="search"
                class="form-control"
                placeholder="Search treks..."
            >

        </div>

    </div>

    <table class="table table-bordered table-striped table-hover align-middle">

        <thead>

            <tr>

                <th>ID</th>
                <th>Trek</th>
                <th>Location</th>
                <th>Difficulty</th>
                <th>Start Date</th>
                <th>Slots</th>
                <th>Status</th>
                <th>Assigned Staff</th>
                <th>Assign Staff</th>
                <th>Trek Actions</th>

            </tr>

        </thead>

        <tbody>

            <tr
                v-for="trek in filteredTreks"
                :key="trek.id"
            >

                <td>{{ trek.id }}</td>

                <td>{{ trek.name }}</td>

                <td>{{ trek.location }}</td>

                <td>{{ trek.difficulty }}</td>

                <td>{{ trek.start_date?.slice(0,10)}}</td>

                <td>{{ trek.available_slots }}</td>

                <td>{{ trek.status }}</td>

                <td>{{ trek.assigned_staff }}</td>

                <td>

                    <select
                        class="form-select mb-2"
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

                    <button
                        class="btn btn-primary btn-sm w-100"
                        @click="assignStaff(trek)"
                    >

                        Assign

                    </button>

                </td>

                 <td>

                    <div class="d-grid gap-2">

                        <button
                            class="btn btn-warning btn-sm"
                            @click="editTrek(trek)"
                        >

                            Edit

                        </button>

                        <button
                            class="btn btn-danger btn-sm"
                            @click="deleteTrek(trek.id)"
                        >

                            Delete

                        </button>

                    </div>

                </td>

            </tr>

        </tbody>

    </table>

</div>

</template>

<script setup>

import { useRouter } from "vue-router"

import { ref, onMounted, computed } from "vue"

import api from "../services/api"

const trekList = ref([])

const staffList = ref([])

const search = ref("")

const editingId = ref(null)

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

const filteredTreks = computed(() => {

    if (!search.value.trim()) {

        return trekList.value

    }

    const query = search.value.toLowerCase()

    return trekList.value.filter(trek =>

        trek.name.toLowerCase().includes(query) ||

        trek.location.toLowerCase().includes(query) ||

        trek.difficulty.toLowerCase().includes(query) ||

        trek.status.toLowerCase().includes(query)

    )

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

    if (editingId.value) {

        await api.put(

            `/admin/treks/${editingId.value}`,

            form.value

        )

        alert("Trek updated successfully.")

    }

    else {

        await api.post(

            "/admin/treks",

            form.value

        )

        alert("Trek created successfully.")

    }

    editingId.value = null

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


async function deleteTrek(trekId) {

    if (!confirm("Delete this trek permanently?")) {

        return

    }

    try {

        await api.delete(

            `/admin/treks/${trekId}`

        )

        alert("Trek deleted successfully.")

        loadTreks()

    }

    catch (error) {

        console.log(error)

        alert("Unable to delete trek.")

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

function editTrek(trek) {

    editingId.value = trek.id

    form.value = {

        name: trek.name,

        location: trek.location,

        description: trek.description,

        difficulty: trek.difficulty,

        duration: trek.duration,

        available_slots: trek.available_slots,

        start_date: trek.start_date?.slice(0, 10),

        end_date: trek.end_date?.slice(0, 10)

    }

    window.scrollTo({

        top: 0,

        behavior: "smooth"

    })

}

function cancelEdit() {

    editingId.value = null

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