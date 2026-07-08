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
    }

];

const router = createRouter({

    history:createWebHistory(),

    routes

});

export default router;