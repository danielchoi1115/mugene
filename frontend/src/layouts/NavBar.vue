<template>
  <ul class="grid gap-6 pt-2 grid-cols-4 bg-white shadow-md dark:bg-gray-800 px-20">
    <button v-for="tab in tabs" :key="tab.key" class="relative px-6 py-3" @click="setCurrentTab(tab.key)">
      <span
        v-if="currentTab === tab.key"
        class="absolute inset-x-0 bottom-0 h-1 mx-10 bg-purple-600 rounded-t-lg"
        aria-hidden="true"
      />
      <div
        class="inline-flex justify-center items-center w-full text-sm font-semibold text-gray-800 transition-colors duration-150 hover:text-gray-800 dark:hover:text-gray-200 dark:text-gray-100"
      >
        <svg
          class="w-5 h-5"
          aria-hidden="true"
          fill="none"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
          />
        </svg>
        <span class="ml-4">{{ tab.description }}</span>
      </div>
    </button>
  </ul>
</template>

<script>
export default {
  data() {
    return {
      currentTab: 'model',
      tabs: [
        {
          key: 'projects',
          description: 'Projects',
        },
        {
          key: 'files',
          description: 'Files',
        },
        {
          key: 'model',
          description: 'Model',
        },
        {
          key: 'reports',
          description: 'Reports',
        },
      ],
    }
  },
  methods: {
    setCurrentTab(key) {
      this.currentTab = key
    },
  },
}
</script>
