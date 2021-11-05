import { createRouter, createWebHistory } from "vue-router";
import Home from "./components/Home";
import Create from "./components/Create";
import EditPage from "./components/EditPage";
import ArticleDetails from "./components/ArticleDetails";

// define routes
const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/create",
    name: "create",
    component: Create,
  },
  {
    path: "/details/:id",
    name: "details",
    component: ArticleDetails,
    props: true,
  },
  {
    path: "/edit/:id",
    name: "edit",
    component: EditPage,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
