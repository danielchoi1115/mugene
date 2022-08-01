<template>
  <h1>{{ msg }}</h1>

  <h3>Installed CLI Plugins</h3>

  <h3>Ecosystem</h3>
  <ul>
    <li>
      <a href="https://router.vuejs.org" target="_blank" rel="noopener">vue-router</a>
    </li>
    <li>
      <a href="https://vuex.vuejs.org" target="_blank" rel="noopener">vuex</a>
    </li>
    <li>
      <a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank" rel="noopener">vue-devtools</a>
    </li>
    <li>
      <a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener">vue-loader</a>
    </li>
    <li>
      <a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">awesome-vue</a>
    </li>
  </ul>
  <div class="pt-6 space-y-4">
    <blockquote>
      <p class="text-lg font-semibold">
        “Tailwind CSS is the only framework that I've seen scale on large teams. It’s easy to customize, adapts to any
        design, and the build size is tiny.”
      </p>
    </blockquote>
    <figcaption class="font-medium">
      <div class="text-blue-800">Sarah Dayan</div>
      <li>haha</li>
      <li>haha2</li>
      <div>Staff Engineer, Algolia</div>
    </figcaption>
  </div>
  <button @click="count++">Add 1</button>
  <p>Count is: {{ count }}</p>
</template>

<script>
let defaultStringType = {
  type: String,
  default: 'Untitled',
}

export default {
  name: 'HelloWorld',
  props: {
    msg: defaultStringType,
  },
  data() {
    return {
      count: 0,
    }
  },
}
</script>
