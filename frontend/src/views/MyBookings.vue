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

    <h2>My Bookings</h2>

    <table class="table table-bordered table-striped mt-4">

        <thead>

            <tr>

                <th>ID</th>

                <th>Trek</th>

                <th>Location</th>

                <th>Booking Status</th>

                <th>Booking Date</th>

                <th>Price</th>

                <th>Payment Status</th>

                <th>Action</th>

                

            </tr>

        </thead>

        <tbody>

            <tr
                v-for="booking in bookings"
                :key="booking.booking_id"
            >

                <td>{{ booking.booking_id }}</td>

                <td>{{ booking.trek_name }}</td>

                <td>{{ booking.location }}</td>

                <td>{{ booking.booking_status }}</td>

                <td>{{ booking.booking_date }}</td>
                
                <td>₹3500</td>

                <td>{{ booking.payment_status }}</td>

                <td>

                    <button
                        v-if="
                            booking.booking_status === 'Booked' &&
                            booking.payment_status === 'Pending'
                        "
                        class="btn btn-success btn-sm"
                        @click="payNow(booking.booking_id)"
                    >

                        Pay ₹3500

                    </button>

                    <span
                        v-else-if="booking.payment_status === 'Paid'"
                        class="text-success fw-bold"
                    >

                        ✔ Paid

                    </span>

                    <span
                        v-else
                        class="text-muted"
                    >

                        —

                    </span>

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

const bookings = ref([])

async function loadBookings() {

    const response = await api.get("/trekker/bookings")

    bookings.value = response.data

}


async function payNow(id) {

    try {

        const response = await api.patch(

            `/trekker/bookings/${id}/payment`

        )

        alert(response.data.message)

        loadBookings()

    }

    catch (error) {

        console.log(error)

        alert("Unable to process payment.")

    }

}

function logout() {

    localStorage.clear()

    router.push("/")

}

onMounted(() => {

    loadBookings()

})

</script>