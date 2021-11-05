<template>
  <div class="container mt-5">
    <h2>{{ article.title }}</h2>
    <p>{{ article.body }}</p>
    <p>Published Date : {{ article.date }}</p>
    <button class="btn btn-danger mx-3 mt-3" @click="deleteById">Delete</button>
    <button class="btn btn-secondary mx-3 mt-3">Edit</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      article: [],
    };
  },
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  methods: {
    deleteById() {
      fetch("http://localhost:8000/delete/" + this.id + "/", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then(() => {
          // redirect to home
          this.$router.push({
            name: "home",
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getArticleData() {
      fetch("http://localhost:8000/get/" + this.id + "/", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        // redirect to home
        .then((resp) => resp.json())
        .then((data) => {
          this.article = data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getArticleData();
  },
};
</script>

<style></style>
