<template>
  <div class="container mt-5">
    <div v-for="res in articles" :key="res.id">
      <h3>
        <router-link :to="{ name: 'details', params: { id: res.id } }">
          {{ res.title }}
        </router-link>
      </h3>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      articles: [],
    };
  },
  methods: {
    getArticles() {
      fetch("http://localhost:8000/", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.articles.push(...data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getArticles();
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
