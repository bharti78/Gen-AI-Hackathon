"use client";
import React, { createContext, useState } from "react";

type SidebarItem = {
  title: string;
  id: string;
};

type ChatBotContextType = {
  isSidebarOpen: boolean;
  toggleSidebar: (value: boolean) => void;
  sidebarData: SidebarItem[];
  setSidebarData: (value: string) => void;
  setSidebarArray: (value: any[]) => void;
  isloading: boolean;
  setIsLoading: (value: boolean) => void;
};

const initialSidebarData: SidebarItem[] = [];

const ChatBotContext = createContext<ChatBotContextType>({
  isSidebarOpen: false,
  toggleSidebar: () => {},
  sidebarData: initialSidebarData,
  setSidebarData: () => {},
  setSidebarArray: () => {},
  isloading: false,
  setIsLoading: () => {},
});

type Props = {
  children: React.ReactNode;
};

export const ChatBotContextProvider: React.FC<Props> = (props) => {
  const [isSidebarOpen, setIsSidebarOpen] = useState<boolean>(false);
  const [isloading, setIsLoading] = useState<boolean>(false);
  const [sidebarData, setSidebarData] =
    useState<SidebarItem[]>(initialSidebarData);

  const onSetIsSidebarOpen = (value: boolean) => {
    setIsSidebarOpen(value);
  };

  const onSetSidebarData = (value: string) => {
    const [id, title] = value.split("_");
    console.log(value, "setting");
    setSidebarData((prev) => {
      prev.push({ title, id });
      return [...prev];
    });
  };

  const onsetSidebarArray = (value: any[]) => {
    // Ensure value is an array
    if (!Array.isArray(value)) {
      console.warn('setSidebarArray received non-array value:', value);
      setSidebarData([]);
      return;
    }
    
    const newArray = value
      .filter((item): item is { id: number; name: string; created_at: string; user: string } => 
        item && typeof item === 'object' && 'name' in item && 'id' in item
      )
      .map((item) => {
        // Extract title from the name (everything after the underscore)
        const nameParts = item.name.split("_");
        const title = nameParts.length > 1 ? nameParts.slice(1).join("_") : item.name;
        
        return {
          title,
          id: item.id.toString(), // Use the numeric ID as a string for the URL
        };
      });
    setSidebarData(newArray);
  };

  const onSetIsLoading = (value: boolean) => {
    setIsLoading(value);
  };

  return (
    <ChatBotContext.Provider
      value={{
        isSidebarOpen,
        toggleSidebar: onSetIsSidebarOpen,
        sidebarData,
        setSidebarData: onSetSidebarData,
        setSidebarArray: onsetSidebarArray,
        isloading,
        setIsLoading: onSetIsLoading,
      }}
    >
      {props.children}
    </ChatBotContext.Provider>
  );
};

export default ChatBotContext;
