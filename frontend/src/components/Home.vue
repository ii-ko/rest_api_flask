<template>
  <div class="container mt-5">
    <div v-for="res in articles" :key="res.id">
      <h3>
        <router-link class="link-style" :to="{ name: 'details', params: { id: res.id } }">
          {{ res.title }}
        </router-link>
      </h3>
      <hr />
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
.link-style {
  font-weight: bold;
  color: black;
  text-decoration: none;
}

.link-style:hover {
  color: gray;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
