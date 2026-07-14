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

    <div class="row mb-3">

        <div class="col-md-5">

            <input
                v-model="search"
                class="form-control"
                placeholder="Search users..."
            >

        </div>

    </div>

    <table class="table table-bordered table-striped">

        <thead>

            <tr>

                <th>ID</th>

                <th>Name</th>

                <th>Email</th>

                <th>Phone</th>

                <th>Status</th>

                <th>Action</th>

            </tr>

        </thead>

        <tbody>

            <tr
                v-for="user in filteredUsers"
                :key="user.id"
            >

                <td>{{ user.id }}</td>

                <td>{{ user.name }}</td>

                <td>{{ user.email }}</td>

                <td>{{ user.phone }}</td>

                <td>

                    <span
                        :class="user.active ? 'text-success' : 'text-danger'"
                    >

                        {{ user.active ? "Active" : "Inactive" }}

                    </span>

                </td>

                <td>

                    <button
                        class="btn btn-sm"
                        :class="user.active ? 'btn-danger' : 'btn-success'"
                        @click="toggleStatus(user)"
                    >

                        {{ user.active ? "Deactivate" : "Activate" }}

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

const users = ref([])

const router = useRouter()

const search = ref("")

const filteredUsers = computed(() => {

    if (!search.value.trim()) {

        return users.value

    }

    const query = search.value.toLowerCase()

    return users.value.filter(user =>

        user.name.toLowerCase().includes(query) ||

        user.email.toLowerCase().includes(query) ||

        user.phone.toLowerCase().includes(query)

    )

})


async function loadUsers() {

    const response = await api.get("/admin/users")

    users.value = response.data

}


async function toggleStatus(user) {

    try {

        await api.patch(

            `/admin/users/${user.id}/status`,

            {

                active: !user.active

            }

        )

        loadUsers()

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

    loadUsers()

})

</script>