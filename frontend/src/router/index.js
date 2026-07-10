import { createRouter, createWebHistory } from "vue-router";

import Login from "../views/Login.vue";
import Register from "../views/Register.vue";

import AdminDashboard from "../views/AdminDashboard.vue";
import StaffDashboard from "../views/StaffDashboard.vue";
import TrekkerDashboard from "../views/TrekkerDashboard.vue";
import TrekManagement from "../views/TrekManagement.vue";
import StaffManagement from "../views/StaffManagement.vue";
import Users from "../views/Users.vue"
import Bookings from "../views/Bookings.vue"
import BrowseTreks from "../views/BrowseTreks.vue"
import MyBookings from "../views/MyBookings.vue"
import MyTreks from "../views/MyTreks.vue"
import Participants from "../views/Participants.vue"
import Profile from "../views/Profile.vue"


const routes = [

    {

        path:"/",

        component:Login

    },

    {

        path:"/register",

        component:Register

    },

    {

        path:"/admin",

        component:AdminDashboard

    },

    {

        path:"/staff",

        component:StaffDashboard

    },

    {

        path:"/trekker",

        component:TrekkerDashboard

    },

    {
        path:"/admin/staff",

        component:StaffManagement
    },
        
    {
        path: "/admin/treks",

        component: TrekManagement
    },

    {
        path: "/admin/users",

        component: Users
    },

    {
        path: "/admin/bookings",

        component: Bookings
    },

    {
        path: "/trekker/treks",
        component: BrowseTreks
    },
    
    {
        path: "/trekker/bookings",
        component: MyBookings
    },

    {
        path: "/staff/treks",
        component: MyTreks
    },


    {
        path: "/staff/treks/:trekId/participants",
        component: Participants
    },

    {
        path: "/trekker/profile",
        component: Profile
    },

];

const router = createRouter({

    history:createWebHistory(),

    routes

});


router.beforeEach((to, from, next) => {

    const token = localStorage.getItem("token")

    const role = localStorage.getItem("role")

    if (
        to.path === "/" ||
        to.path === "/register"
    ) {

        if (!token) {

            return next()

        }

        if (role === "admin") {

            return next("/admin")

        }

        if (role === "staff") {

            return next("/staff")

        }

        return next("/trekker")

    }

    if (!token) {

        return next("/")

    }

    if (
        to.path.startsWith("/admin") &&
        role !== "admin"
    ) {

        if (role === "staff") {

            return next("/staff")

        }

        return next("/trekker")

    }

    if (
        to.path.startsWith("/staff") &&
        role !== "staff"
    ) {

        if (role === "admin") {

            return next("/admin")

        }

        return next("/trekker")

    }

    if (
        to.path.startsWith("/trekker") &&
        role !== "trekker"
    ) {

        if (role === "admin") {

            return next("/admin")

        }

        return next("/staff")

    }

    next()

})

export default router;