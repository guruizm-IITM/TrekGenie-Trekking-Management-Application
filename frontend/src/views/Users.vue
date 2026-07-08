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

    <h2>Users</h2>

    <table class="table table-bordered table-striped">

        <thead>

            <tr>

                <th>ID</th>

                <th>Name</th>

                <th>Email</th>

                <th>Phone</th>

                <th>Active</th>

            </tr>

        </thead>

        <tbody>

            <tr
                v-for="user in users"
                :key="user.id"
            >

                <td>{{ user.id }}</td>

                <td>{{ user.name }}</td>

                <td>{{ user.email }}</td>

                <td>{{ user.phone }}</td>

                <td>{{ user.active ? "Yes" : "No" }}</td>

            </tr>

        </tbody>

    </table>

</div>

</template>

<script setup>

import { useRouter } from "vue-router"

import { ref, onMounted } from "vue"

import api from "../services/api"

const users = ref([])

const router = useRouter()

async function loadUsers() {

    const response = await api.get("/admin/users")

    users.value = response.data

}

function logout() {

    localStorage.clear()

    router.push("/")

}

onMounted(() => {

    loadUsers()

})

</script>