import { createRouter, createWebHistory } from "vue-router";

import Login from "../views/Login.vue";
import Register from "../views/Register.vue";

import AdminDashboard from "../views/AdminDashboard.vue";
import StaffDashboard from "../views/StaffDashboard.vue";
import TrekkerDashboard from "../views/TrekkerDashboard.vue";

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

    }

];

const router = createRouter({

    history:createWebHistory(),

    routes

});

export default router;