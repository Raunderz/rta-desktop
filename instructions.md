# Getting Started with Expo & React Native (using Bun)

This project has been set up using [Expo](https://expo.dev/) and [Bun](https://bun.sh/) as the package manager.

## Project Structure

- `app/`: The React Native + Expo project directory.
- `LICENSE`: The project's license.
- `README.md`: Original project overview.
- `instructions.md`: This file.

## How to Run the App

Navigate to the `app/` directory and use Bun to start the development server:

```bash
cd app
bun run start
```

### Platform-Specific Commands

- **Android:** `bun run android`
- **iOS:** `bun run ios` (requires macOS)
- **Web:** `bun run web`

## Moving Forward

### 1. Adding New Dependencies
To add new packages, use `bun add`:

```bash
cd app
bun add <package-name>
# For dev dependencies:
bun add -d <package-name>
```

### 2. Project Organization
Consider organizing your code in `app/src/`:
- `app/src/components/`: Reusable UI components.
- `app/src/screens/`: Main application screens.
- `app/src/navigation/`: Navigation logic (e.g., React Navigation or Expo Router).
- `app/src/hooks/`: Custom React hooks.
- `app/src/utils/`: Utility functions and constants.

### 3. Recommended Tools
- **Expo Go:** Install the "Expo Go" app on your physical device to test the app without a full native build.
- **VS Code Extensions:**
  - `Expo Tools`
  - `ESLint`
  - `Prettier`

### 4. Next Steps
- Update `app/App.js` to start building your UI.
- Explore the [Expo Documentation](https://docs.expo.dev/) for more advanced features like push notifications, camera, and maps.
- If you need navigation, consider setting up [Expo Router](https://docs.expo.dev/router/introduction/).

## Future Architectural & Performance Considerations

To ensure Rta remains fast and responsive on mobile, keep these optimizations and strategies in mind:

### 1. Performance Optimization
- **New Architecture (Fabric):** Enable React Native's New Architecture to benefit from the synchronous UI thread and better performance for the code editor and AI streaming UI.
- **FlashList:** Use `@shopify/flash-list` for the file explorer and Git logs to maintain 60 FPS scrolling even with large datasets.
- **Lightweight State:** Prefer **Zustand** over Redux to keep the JS bundle small and state management simple.
- **Styling:** Use **NativeWind** (Tailwind for React Native) or plain **StyleSheet** to minimize styling overhead.

### 2. Git & Filesystem Integration
- **Isomorphic-Git:** Explore using [isomorphic-git](https://isomorphic-git.org/) for a full Git client implementation in JavaScript.
- **FS Layer:** Pair it with a compatible filesystem layer like `expo-file-system` (may require a shim) or `react-native-fs` to manage repository storage.

### 3. Note on Alternative Frameworks (LynxJS/VanJS)
- **Evaluation:** Evaluated LynxJS + VanJS for extreme startup speed (<200ms TTI) and multi-threaded UI benefits.
- **Current Stance:** Sticking with React Native/Expo for the mature ecosystem (Editor components, Git/FS bridges) and stable development experience. Re-evaluate Lynx as its ecosystem matures, particularly for performance-critical "Core" components.
