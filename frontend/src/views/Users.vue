<template>

<div class="container mt-5">

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

            <<tr
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

import { ref, onMounted } from "vue"

import api from "../services/api"

const users = ref([])

async function loadUsers() {

    const response = await api.get("/admin/users")

    users.value = response.data

}

onMounted(() => {

    loadUsers()

})

</script>