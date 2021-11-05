<template>
  <div class="container mt-4">
    <form action="">
      <input type="text" class="form-control" v-model="title" placeholder="Enter your title here" />
      <textarea row="10" class="form-control" v-model="body" placeholder="Type your article here.."></textarea>
      <button class="btn btn-primary mt-4">Submit</button>
    </form>
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
};
</script>

<style></style>
