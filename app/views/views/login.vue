<template>
  <div class="w-full max-w-md bg-white rounded-lg shadow-md p-8">
    <h2 class="text-2xl font-semibold text-gray-800 text-center mb-6">登入</h2>
    <form class="space-y-4">
      <div>
        <label for="username" class="block text-sm font-medium text-gray-700">使用者名稱：</label>
        <input type="username" id="username" name="username" placeholder="輸入您的使用者名稱" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400" required>
      </div>
      <div>
        <label for="password" class="block text-sm font-medium text-gray-700">密碼：</label>
        <input type="password" id="password" name="password" placeholder="輸入您的密碼" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400" required>
      </div>
      <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded-md font-semibold hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-offset-2">登入</button>
    </form>
    <p class="mt-4 text-sm text-center text-gray-600">
      沒有帳號？<a href="#" class="text-blue-500 hover:underline">註冊</a>
    </p>
  </div>
</template>

<script>
    const { createApp  } = Vue;

    createApp({
        data() {
        },
        mounted() {
        },
        template: document.querySelector('template').innerHTML,
    }).mount('#app')
</script>
