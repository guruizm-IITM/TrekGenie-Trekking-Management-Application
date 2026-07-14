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

    <h2>Staff Management</h2>

    <div class="card p-4 mb-4">

        <h4>Create Staff</h4>

        <input
            v-model="form.name"
            class="form-control mb-2"
            placeholder="Name"
        >

        <input
            v-model="form.email"
            class="form-control mb-2"
            placeholder="Email"
        >

        <input
            v-model="form.password"
            type="password"
            class="form-control mb-2"
            placeholder="Password"
        >

        <input
            v-model="form.phone"
            class="form-control mb-3"
            placeholder="Phone"
        >

        <button
            class="btn btn-success"
            @click="createStaff"
        >
            Create Staff
        </button>

    </div>


    <div class="row mb-3">

        <div class="col-md-5">

            <input
                v-model="search"
                class="form-control"
                placeholder="Search staff..."
            >

        </div>

    </div>

    <table class="table table-bordered table-striped">

        <thead>

            <tr>

                <th>ID</th>

                <th>Name</th>

                <th>Email</th>

                <th>Active</th>

                <th>Action</th>

            </tr>

        </thead>

        <tbody>

            <tr
                v-for="staff in filteredStaff"
                :key="staff.id"
            >

                <td>{{ staff.id }}</td>

                <td>{{ staff.name }}</td>

                <td>{{ staff.email }}</td>

                <td>{{ staff.active ? "Yes" : "No" }}</td>

                <td>

                    <button
                        class="btn btn-warning btn-sm"
                        @click="toggleStatus(staff)"
                    >
                        {{ staff.active ? "Deactivate" : "Activate" }}
                    </button>

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

const staffList = ref([])

const search = ref("")

const form = ref({

    name: "",

    email: "",

    password: "",

    phone: ""

})

const router = useRouter()

const filteredStaff = computed(() => {

    if (!search.value.trim()) {

        return staffList.value

    }

    const query = search.value.toLowerCase()

    return staffList.value.filter(staff =>

        staff.name.toLowerCase().includes(query) ||

        staff.email.toLowerCase().includes(query) ||

        staff.phone.toLowerCase().includes(query)

    )

})

async function loadStaff() {

    const response = await api.get("/admin/staff")

    staffList.value = response.data

}

async function createStaff() {

    await api.post("/admin/staff", form.value)

    form.value = {

        name: "",

        email: "",

        password: "",

        phone: ""

    }

    loadStaff()

}

async function toggleStatus(staff) {

    await api.patch(

        `/admin/staff/${staff.id}/status`,

        {

            active: !staff.active

        }

    )

    loadStaff()

}

function logout() {

    localStorage.clear()

    router.push("/")

}

onMounted(() => {

    loadStaff()

})

</script>