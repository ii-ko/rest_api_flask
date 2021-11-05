<template>
  <div class="container mt-4">
    <h2>Create Form</h2>
    <form @submit.prevent="insertArticle">
      <div class="form-group">
        <input type="text" class="form-control" v-model="title" placeholder="Enter your title here" />
      </div>
      <div class="form-group">
        <textarea row="10" class="form-control" v-model="body" placeholder="Type your article here.." style="height: 350px"></textarea>
      </div>
      <button type="submit" class="btn btn-primary mt-4">Submit</button>
    </form>
    <div v-if="error" class="alert alert-warning alert-dismissible fade show mt-5" role="alert">
      <strong>{{ error }}</strong>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    // model
    return {
      title: null,
      body: null,
      error: null,
    };
  },
  methods: {
    insertArticle() {
      if (!this.title || !this.body) {
        this.error = "Please fill all fields";
      } else {
        fetch("http://localhost:8000/post", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            // fields in db : model
            title: this.title,
            body: this.body,
          }),
        })
          .then((resp) => resp.json())
          .then(() => {
            this.$router.push({
              name: "home",
            });
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>
<style>
.form-group {
  padding: 5px;
}
</style>
