<template lang="en">
  <body class="bg-purple-300 pb-14">
    <div
      class="flex h-screen-90 bg-gray-50 dark:bg-gray-900 mt-10 mx-10 rounded-2xl"
      class:overflow-hidden={isSideMenuOpen}
    >
      <!-- <Sidebar bind:currentTab /> -->
      <SideBar/>
      <div class="flex flex-col flex-1 w-full">
        <!-- <MuHeader bind:isDark /> -->
        <MuHeader></MuHeader>
        <!-- <Navbar bind:currentTab /> -->
        <NavBar></NavBar>
        <main class="h-full overflow-y-auto">
          <!-- <BodyContainer
            bind:currentTab
            bind:savedParameters
            bind:lastParameterId
            bind:lastReportId
            bind:reports
            on:openModal={handleOpenModal}
          /> -->
          <BodyContainer></BodyContainer>
        </main>
      </div>
    </div>

    <PreviewModal bind:open={isModalOpen} bind:reportData={previewData} />
  </body>
<!-- https://dev.to/tonyketcham/vue-tailwind-2-0-dark-mode-using-vuex-localstorage-and-user-s-default-preference-439g -->
</template>

<script>
import { mapGetters } from 'vuex'
import BodyContainer from './layouts/BodyContainer.vue'
import SideBar from './layouts/SideBar.vue'
import NavBar from './layouts/NavBar.vue'
import MuHeader from './layouts/MuHeader.vue'

export default {
  name: 'App',
  components: { SideBar, BodyContainer, NavBar, MuHeader },
  data() {
    return {
      isDark: true,
    }
  },
  computed: {
    ...mapGetters({ theme: 'getTheme' }),
  },
  watch: {
    theme(newTheme, oldTheme) {
      newTheme === 'light'
        ? document.querySelector('html').classList.remove('dark')
        : document.querySelector('html').classList.add('dark')
    },
  },
  beforeMount() {
    this.$store.dispatch('initTheme')
  },
  methods: {
    greet(event) {
      // `this` inside methods points to the current active instance
      alert(`Hello ${this.name}!`)
      // `event` is the native DOM event
      if (event) {
        alert(event.target.tagName)
      }
    },
  },
}
</script>

<style></style>
