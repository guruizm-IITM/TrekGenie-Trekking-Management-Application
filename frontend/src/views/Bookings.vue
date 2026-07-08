<template>

<div class="container mt-5">

    <h2>Bookings</h2>

    <table class="table table-bordered table-striped">

        <thead>

            <tr>

                <th>ID</th>

                <th>Trekker</th>

                <th>Trek</th>

                <th>Booking Status</th>

                <th>Payment</th>

                <th>Date</th>

            </tr>

        </thead>

        <tbody>

            <tr
                v-for="booking in bookings"
                :key="booking.booking_id"
            >

                <td>{{ booking.booking_id }}</td>

                <td>{{ booking.trekker }}</td>

                <td>{{ booking.trek }}</td>

                <td>{{ booking.booking_status }}</td>

                <td>{{ booking.payment_status }}</td>

                <td>{{ booking.booking_date }}</td>

            </tr>

        </tbody>

    </table>

</div>

</template>

<script setup>

import { ref, onMounted } from "vue"

import api from "../services/api"

const bookings = ref([])

async function loadBookings() {

    const response = await api.get("/admin/bookings")

    bookings.value = response.data

}

onMounted(() => {

    loadBookings()

})

</script>