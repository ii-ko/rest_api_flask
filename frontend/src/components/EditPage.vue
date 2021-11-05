<template>
  <div class="container mt-4">
    <h2>Edit Form</h2>
    <form @submit.prevent="insertArticle">
      <div class="form-group">
        <input type="text" class="form-control" v-model="title" placeholder="Enter your title here" />
      </div>
      <div class="form-group">
        <textarea row="10" class="form-control" v-model="body" placeholder="Type your article here.." style="height: 350px"></textarea>
      </div>
      <button type="submit" class="btn btn-primary mt-4">Update</button>
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

  beforeRouteEnter(to, from, next) {
    if (to.params.id != undefined) {
      fetch("http://localhost:8000/get/" + to.params.id + "/", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          return next((vm) => ((vm.title = data.title), (vm.body = data.body)));
        })
        .catch((error) => {
          console.log(error);
        });
    } else {
      return next();
    }
  },
};
</script>

<style></style>
